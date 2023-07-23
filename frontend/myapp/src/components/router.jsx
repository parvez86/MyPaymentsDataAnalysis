import React from 'react'
import {
    BrowserRouter,
    Routes, Route
  } from "react-router-dom";
import App from '../App';
import InstalledApps from './page/installedApps';


const Router = () => {
  return (
        <BrowserRouter>
            <Routes>
                <Route exact path='' element={<App/>}/>
                <Route exact path='/stats/:id1/:id2' element={<InstalledApps/>}/>
            </Routes>
        </BrowserRouter>
  )
}

export default Router