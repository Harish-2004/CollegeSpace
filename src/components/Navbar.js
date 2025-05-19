import React from 'react';
import './Navbarcss.css';
import { useNavigate } from 'react-router-dom';

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogin = () => {
    navigate('/Login');
  };

  const handleSignup = () => {
    navigate('/Signup');
  };

  return (
    <div>
      <nav>
        <div id="cont">
          CollegeSpace
        </div>
        <div>
          <ul id="navbar">
            <li>
              <button 
                id='n' 
                onClick={handleLogin}
                className="nav-button"
              >
                Login
              </button>
            </li>
            <li>
              <button 
                id='n' 
                onClick={handleSignup}
                className="nav-button"
              >
                Signup
              </button>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
};

export default Navbar; 