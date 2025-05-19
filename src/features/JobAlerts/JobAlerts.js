import React from 'react';
import './JobAlerts.css';

const JobAlerts = () => {
  return (
    <div className="job-alerts-container">
      <h2>Job and Internship Alerts</h2>
      <div className="job-categories">
        <div className="on-campus">
          <h3>On-Campus Opportunities</h3>
          <div className="job-box">
            <ul>
              <li>
                <h5>Bloomberg</h5>
                <span>Software Engineering Intern - Stipend: INR 35,000/month</span>
                <p>Develop impactful solutions to complex, real-world problems and make an immediate impact on global markets.</p>
                <form action="https://unstop.com/internships/software-engineering-internship-bloomberg-838547">
                  <button type="submit">Apply now</button>
                </form>
              </li>
              <li>
                <h5>Microsoft</h5>
                <span>Software Development Intern - Stipend: INR 40,000/month</span>
                <p>Work on cutting-edge technologies and contribute to Microsoft's products and services.</p>
                <form action="https://careers.microsoft.com">
                  <button type="submit">Apply now</button>
                </form>
              </li>
            </ul>
          </div>
        </div>

        <div className="off-campus">
          <h3>Off-Campus Opportunities</h3>
          <div className="job-box">
            <ul>
              <li>
                <h5>Taxing Ninjas</h5>
                <span>Web Developer Intern - Stipend: INR 25,000/month</span>
                <p>Work on modern web applications and gain hands-on experience with real-world projects.</p>
                <form action="https://unstop.com/internships">
                  <button type="submit">Apply now</button>
                </form>
              </li>
              <li>
                <h5>Google Summer of Code</h5>
                <span>Open Source Contributor - Stipend: $3000</span>
                <p>Work with open source organizations and contribute to meaningful projects.</p>
                <form action="https://summerofcode.withgoogle.com">
                  <button type="submit">Apply now</button>
                </form>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default JobAlerts; 