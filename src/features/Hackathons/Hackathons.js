import React from 'react';
import './Hackathons.css';

const Hackathons = () => {
  return (
    <div className="hackathons-container">
      <h2>Upcoming Hackathons</h2>
      <div className="hackathons-box">
        <ul>
          <li>
            <h5>Hardware Hackathon @ VNR College</h5>
            <div className="hackathon-details">
              <p className="date">End Date: 15 Dec 23, 04:00 PM IST</p>
              <p className="description">A 48-hour hardware hackathon focusing on IoT and embedded systems.</p>
              <div className="prizes">
                <span>Prizes: ₹50,000</span>
              </div>
            </div>
            <form action="https://unstop.com/hackathons/hardware-hackathon-convergence-2023r-vallurupalli-nageswara-rao-vignana-jyothi-institute-of-engineering-techn-835500">
              <button type="submit">Register Now</button>
            </form>
          </li>
          <li>
            <h5>Innovasia - National Level Hackathon @ Vasavi College</h5>
            <div className="hackathon-details">
              <p className="date">End Date: 21 Dec 23, 04:00 PM IST</p>
              <p className="description">A national-level hackathon focusing on AI/ML and blockchain solutions.</p>
              <div className="prizes">
                <span>Prizes: ₹1,00,000</span>
              </div>
            </div>
            <form action="https://unstop.com/hackathons">
              <button type="submit">Register Now</button>
            </form>
          </li>
          <li>
            <h5>CodeFest 2023 - International Hackathon</h5>
            <div className="hackathon-details">
              <p className="date">End Date: 30 Dec 23, 11:59 PM IST</p>
              <p className="description">An international hackathon focusing on sustainable development goals.</p>
              <div className="prizes">
                <span>Prizes: $10,000</span>
              </div>
            </div>
            <form action="https://codefest.com">
              <button type="submit">Register Now</button>
            </form>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Hackathons; 