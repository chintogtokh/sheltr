import {suburbConstants } from '../constants';

export const suburbActions = {
    fetchSuburb,
    fetchSuburbWiki
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

function toTitleCase(str)
{
    return str.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
}

function fetchSuburbWiki (suburb_shim) {
    var url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + toTitleCase(suburb_shim.replace("-"," ")) + ", Victoria";
    return dispatch => {
    fetch(url)
        .then(response => response.json().then( data => ({
            data: data,
            status: response.status
            })
        ))
        .then(response => {
            if (response.status !== 200) {
                dispatch({
                    type: suburbConstants.SUBURB_WIKI_NOTFOUND,
                })
            }
            else{
                dispatch({
                    type: suburbConstants.FETCH_SUBURB_WIKI,
                    payload: response.data
                })
            }
        });
    };
};