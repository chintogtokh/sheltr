import {suburbConstants } from '../constants';

export const suburbActions = {
    fetchSuburb
};

function fetchSuburb (suburb_shim) {
	return dispatch => {
    fetch('/suburbs/' + suburb_shim)
        .then(response => response.json().then( data => ({
            data: data,
            status: response.status
            })
        ))
        .then(response => {
            if (response.status !== 200) {
                dispatch({
                    type: suburbConstants.SUBURB_NOTFOUND,
                })
            }
            else{
                dispatch({
                    type: suburbConstants.FETCH_SUBURB,
                    payload: response.data
                })
            }
        });
	};
};