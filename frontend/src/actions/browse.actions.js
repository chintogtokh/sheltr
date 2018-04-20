import {
    browseConstants
} from '../constants';

export const browseActions = {
    browseSuburb
};

function browseSuburb(data) {

    return dispatch => {
        fetch('https://jsonplaceholder.typicode.com/posts', {
                method: 'POST',
                headers: {
                    'content-type': 'application/json'
                },
                body: JSON.stringify(data)
            }).then(res => res.json())
            .then(posts =>
                dispatch({
                    type: browseConstants.BROWSE_SUBURBS,
                    payload: data
                })
            );

    }
};