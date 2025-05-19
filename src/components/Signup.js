import React from 'react';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Signup() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    startYear: '',
    branch: '',
    contactno: '',
    password: '',
    email: '',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    try {
      const response = await fetch("http://localhost:5001/createUser", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          name: formData.name,
          email: formData.email,
          password: formData.password,
          contactno: formData.contactno,
          startYear: formData.startYear,
          branch: formData.branch
        })
      });

      const data = await response.json();
      
      if (data.success) {
        alert('User created successfully!');
        navigate('/Login');
      } else {
        alert('Failed to create user. Please try again.');
      }
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred. Please try again.');
    }
  };

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Sign Up</h2>
      <form style={styles.form} onSubmit={handleSubmit}>
        <label style={styles.label}>Name:</label>
        <input
          type="text"
          name="name"
          value={formData.name}
          onChange={handleInputChange}
          style={styles.input}
          required
        />

        <label style={styles.label}>Batch Start Year:</label>
        <input
          type="text"
          name="startYear"
          value={formData.startYear}
          onChange={handleInputChange}
          style={styles.input}
          required
        />

        <label style={styles.label}>Branch:</label>
        <input
          type="text"
          name="branch"
          value={formData.branch}
          onChange={handleInputChange}
          style={styles.input}
          required
        />

        <label style={styles.label}>Password:</label>
        <input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleInputChange}
          style={styles.input}
          required
        />

        <label style={styles.label}>Email:</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleInputChange}
          style={styles.input}
          required
        />

        <label style={styles.label}>Contact No:</label>
        <input
          type="text"
          name="contactno"
          value={formData.contactno}
          onChange={handleInputChange}
          style={styles.input}
          required
        />

        <button type="submit" style={styles.button}>
          Sign Up
        </button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    width: '60%',
    margin: 'auto',
    padding: '20px',
    border: '1px solid #ccc',
    borderRadius: '5px',
    marginTop: '50px',
  },
  title: {
    textAlign: 'center',
    marginBottom: '20px',
  },
  form: {
    display: 'flex',
    flexDirection: 'column',
  },
  label: {
    marginBottom: '8px',
  },
  input: {
    padding: '8px',
    marginBottom: '16px',
    border: '1px solid #ccc',
    borderRadius: '3px',
  },
  button: {
    backgroundColor: '#4caf50',
    color: 'white',
    padding: '10px',
    cursor: 'pointer',
    borderRadius: '3px',
    border: 'none',
  },
};