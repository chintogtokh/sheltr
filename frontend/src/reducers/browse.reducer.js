import {browseConstants} from '../constants';

const initialState = {
	browsePreferences: {}
}

export function browse(state = initialState, action) {
	switch(action.type){
		case browseConstants.BROWSE_SUBURBS:
			return {
				...state,
				browsePreferences: action.payload
			}
		default:
		return state;
	}
}