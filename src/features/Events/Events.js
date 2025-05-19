import React from 'react';
import './Events.css';

const Events = () => {
  return (
    <div className="events-container">
      <h2>Upcoming Events</h2>
      <div className="events-box">
        <ul>
          <li>
            <h5>Vasavi Winter MUN</h5>
            <div className="event-details">
              <p className="date">Date: 10-12 Dec 2023</p>
              <p className="venue">Venue: Vasavi College of Engineering</p>
              <p className="description">Model United Nations conference focusing on global issues and diplomacy.</p>
            </div>
            <form action="https://vasavi.edu.in/events">
              <button type="submit">Register Now</button>
            </form>
          </li>
          <li>
            <h5>Tech Symposium 2023</h5>
            <div className="event-details">
              <p className="date">Date: 15-17 Dec 2023</p>
              <p className="venue">Venue: VNR College of Engineering</p>
              <p className="description">Annual technical symposium featuring workshops, competitions, and expert talks.</p>
            </div>
            <form action="https://vnrvjiet.ac.in/events">
              <button type="submit">Register Now</button>
            </form>
          </li>
          <li>
            <h5>Cultural Fest 2023</h5>
            <div className="event-details">
              <p className="date">Date: 20-22 Dec 2023</p>
              <p className="venue">Venue: Vasavi College of Engineering</p>
              <p className="description">Annual cultural festival featuring music, dance, drama, and art competitions.</p>
            </div>
            <form action="https://vasavi.edu.in/events">
              <button type="submit">Register Now</button>
            </form>
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Events; 