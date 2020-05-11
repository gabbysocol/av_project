  
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './serviceWorker';
// import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, 
    document.getElementById('root'));
    
registerServiceWorker();