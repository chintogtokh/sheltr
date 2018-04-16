import {suburbConstants} from '../constants';

const initialState = {
	suburb: {}
}

export function suburb(state = initialState, action) {
	switch(action.type){
		case suburbConstants.FETCH_SUBURB:
			return {
				...state,
				suburb: action.payload
			}
		case suburbConstants.SUBURB_NOTFOUND:
			return {
				error: 'Suburb not found'
			}
		default:
		return state;
	}
}