import React from 'react';
import './Whatwedo.css'
import { Link } from 'react-router-dom';
export default function Afterlogin() {
  return <div className='conta'>
    <nav>
      <div id="cont">
        CollegeSpace
      </div>
      <div>
        <ul id="navbar">
          <li  id='f'><Link to="/Interview">Interview Experiences</Link></li>
          <li  id='f'><Link to="http://localhost:5000">Chatrooms</Link></li>
          <li  id='f'><Link to="/">Student Profiles</Link></li>
          <button >Logout</button>
        </ul>
      </div>
    </nav>
    <div>
      <h2>Job and Internship Alerts</h2>    
      <div className='box'>
        <ul>
          <li>
          >> <h5>Bloomberg</h5><span>is currently looking for Software Engineering Intern who will develop impactful solutions to complex, real-world problems and make an immediate impact on global markets.
          They will also take ownership of their projects under the mentorship of full-time software engineers.
          Stipend:- INR 35,000 </span>
          <form action="https://unstop.com/internships/software-engineering-internship-bloomberg-838547?utm_source=Internships&utm_medium=D2C-Newsletters&utm_campaign=Eng-3rd-Year">
            <button type="submit">Apply now</button>
          </form>
          </li>
          <li>
          >> <h5>Taxing Ninjas is hiring Web Developer Interns, Apply Now!</h5>
          <form action="https://unstop.com/internships/software-engineering-internship-bloomberg-838547?utm_source=Internships&utm_medium=D2C-Newsletters&utm_campaign=Eng-3rd-Year">
            <button type="submit">Apply now</button>
          </form>
          </li>
          

        </ul>
      </div>
    </div>
    <div>
      <h2>Upcoming Hackatons and coding contest</h2>    
      <div className='box'>
        <ul>
        <li>
          >> <h5>Hardware Hackaton @ VNR College</h5>
          <p> End Date 15 Dec 23, 04:00 PM IST</p>
          <form action="https://unstop.com/hackathons/hardware-hackathon-convergence-2023r-vallurupalli-nageswara-rao-vignana-jyothi-institute-of-engineering-techn-835500">
            <button type="submit">Apply now</button>
          </form>
          </li>
          <li>
          >> <h5>Innovasia ,A National Level Hackaton @ Vasavi College</h5>
          <p> End Date 21 Dec 23, 04:00 PM IST</p>
          <form action="https://unstop.com/hackathons/hardware-hackathon-convergence-2023r-vallurupalli-nageswara-rao-vignana-jyothi-institute-of-engineering-techn-835500">
            <button type="submit">Apply now</button>
          </form>
          </li>
        </ul>
      </div>
    </div>
    <div>
      <h2>Upcoming Events</h2>    
      <div className='box' >
        <ul>
          <li>>> Vasavi Winter MUN</li>
        </ul>
      </div>
    </div>

  </div>
}
