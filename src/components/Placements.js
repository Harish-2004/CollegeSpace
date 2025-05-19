import React, { useState, useEffect } from 'react';
import StudentCard from './StudentCard';
import axios from 'axios';
import { API_BASE_URL } from '../config';

export default function Placements(){
    const [students, setStudents] = useState([]);
    useEffect(()=> {
      axios.get(`${API_BASE_URL}/load`)
        .then(response => {
         const responseData = response.data;
         setStudents(responseData)
          console.log(responseData);
        })
        .catch(error => {
          console.error(error);
        });
    }, []);
return (<div>
      <h1>Student Cards</h1>

      {students.map(student => (
        <StudentCard key={student._id} student={student} />
      ))}
      
    </div>
  );
};

