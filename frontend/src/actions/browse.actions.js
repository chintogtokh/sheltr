import {
    browseConstants
} from '../constants';

export const browseActions = {
    enterPreferences,
    fetchRankedSuburbs
};

function enterPreferences(data) {

    return { type: browseConstants.ENTERED_PREFERENCES,
            payload: data };

};

function fetchRankedSuburbs(){

	return dispatch => {
    fetch('/api/ranked_suburbs')
        .then(response => response.json().then( data => ({
            data: data,
            status: response.status
            })
        ))
        .then(response => {
            if (response.status !== 200) {
                // dispatch({
                //     type: suburbConstants.SUBURB_NOTFOUND,
                // })
            }
            else{
                dispatch({
                    type: browseConstants.FETCH_RANKED_SUBURBS,
                    payload: response.data
                })
            }
        });
	};


}