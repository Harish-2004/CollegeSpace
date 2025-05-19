import React, { useState } from 'react';
import './InterviewForm.css'; 
import { useNavigate } from 'react-router-dom';
import { API_BASE_URL } from '../config';

export default function Intform()
{const navigate=useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    contactNo: '',
    companyName: '',
    package: '',
    rounds: '',
    coding: '',
    csConcepts: '',
    hr: '',
    suggestions: '',
  });
const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async(e) => {
    e.preventDefault();
    const respons = await fetch(`${API_BASE_URL}/createInt`, {
      method: 'POST',
      headers:
      {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name:formData.name,
        email:formData.email,
        companyName:formData.companyName,
        contactno:formData.contactno,
        rounds:formData.rounds,
        coding:formData.coding,
        csConcepts:formData.csConcepts,
        hr:formData.hr,
        suggestions:formData.suggestions,

      })
    });
    
    const j = await respons.json();
    console.log(j);

    if (!j.success) alert('enter correct credentials')
    else {
      navigate('/Interview')
    }
   
   
  };

  return (
    <div className="form-container">
      <h2>Interview Experience Form</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" name="name" value={formData.name} onChange={handleChange} />
        </label>
        <label>
          Email:
          <input type="email" name="email" value={formData.email} onChange={handleChange} />
        </label>
        <label>
          Contact No:
          <input type="text" name="contactNo" value={formData.contactNo} onChange={handleChange} />
        </label>
        <label>
          Company Name:
          <input type="text" name="companyName" value={formData.companyName} onChange={handleChange} />
        </label>
        <label>
          Package:
          <input type="text" name="package" value={formData.package} onChange={handleChange} />
        </label>
        <label>
          Rounds:
          <input type="text" name="rounds" value={formData.rounds} onChange={handleChange} />
        </label>
        <label>
          Coding:
          <textarea name="coding" value={formData.coding} onChange={handleChange} />
        </label>
        <label>
          CS Concepts:
          <textarea name="csConcepts" value={formData.csConcepts} onChange={handleChange} />
        </label>
        <label>
          HR:
          <textarea name="hr" value={formData.hr} onChange={handleChange} />
        </label>
        <label>
          Suggestions or Extra details:
          <textarea name="suggestions" value={formData.suggestions} onChange={handleChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};
