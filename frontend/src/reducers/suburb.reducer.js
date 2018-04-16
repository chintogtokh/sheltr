import {suburbConstants} from '../constants';

const initialState = {
	suburb: {},
	suburb_wiki: {}
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
		case suburbConstants.FETCH_SUBURB_WIKI:
			return {
				...state,
				suburb_wiki: action.payload
			}
		case suburbConstants.SUBURB_WIKI_NOTFOUND:
			return {
				error: 'Suburb wiki not found'
			}
		default:
		return state;
	}
}