import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import App from './components/app/App';
import registerServiceWorker from './registerServiceWorker';
import {createStore, applyMiddleware } from 'redux';
import { store } from './helpers';

// setup fake backend
import { configureFakeBackend } from './helpers';
configureFakeBackend();

ReactDOM.render(
	<Provider store={store}>
		<App />
	</Provider>,
	document.getElementById('root')
	);
registerServiceWorker();