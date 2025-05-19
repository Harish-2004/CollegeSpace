import React from 'react';
import App from './App'
import Login from './components/Login'
import Afterlogin from './components/Afterlogin';
import Signup from './components/Signup';
import Interview from './features/Interview/Interview'
import Intform from './components/Intform'
import StudentProfile from './features/StudentProfile/StudentProfile'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

export default function Main()
{ return <Router>
      <div>
        <Routes>
          <Route exact path="/" element={<App/>} />
          <Route exact path="/Login"  element={<Login/>}/>
          <Route exact path="/Afterlogin"  element={<Afterlogin/>}/>
          <Route exact path="/Signup"  element={<Signup/>}/>
          <Route exact path='/Interview' element={<Interview/>}/>
          <Route exact path='/Intform' element={<Intform/>}/>
          <Route exact path='/StudentProfile' element={<StudentProfile/>}/>
        </Routes>
      </div>
    </Router>
}