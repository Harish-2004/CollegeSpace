import React from 'react';
import './Whatwedo.css'
import { Link } from 'react-router-dom';
import JobAlerts from '../features/JobAlerts/JobAlerts';
import Hackathons from '../features/Hackathons/Hackathons';
import Events from '../features/Events/Events';
import InterviewPrep from '../features/InterviewPrep/InterviewPrep';
import { CHAT_URL } from '../config';

export default function Afterlogin() {
  return <div className='conta'>
    <nav>
      <div id="cont">
        CollegeSpace
      </div>
      <div>
        <ul id="navbar">
          <li  id='f'><Link to="/Interview">Interview Experiences</Link></li>
          <li  id='f'><Link to={CHAT_URL}>Chatrooms</Link></li>
          <li  id='f'><Link to="/StudentProfile">Student Profile</Link></li>
          <button >Logout</button>
        </ul>
      </div>
    </nav>
    
    <div className="main-content">
      <JobAlerts />
      <Hackathons />
      <Events />
      <InterviewPrep />
    </div>
  </div>
}
