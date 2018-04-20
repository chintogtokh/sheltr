import {browseConstants} from '../constants';

const initialState = {
	browsePreferences: {}
}

export function browse(state = {}, action) {
	switch(action.type){
		case browseConstants.ENTERED_PREFERENCES:
			return {
				browsePreferences: action.payload
			}
		default:
		return state;
	}
}