import React, { useEffect, useState } from 'react';

const Users = () => {
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setUsers(results);
        console.log('Users API endpoint:', apiUrl);
        console.log('Fetched users:', results);
      });
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <ul className="list-group">
        {users.map((user, idx) => (
          <li className="list-group-item" key={idx}>
            {user.name} - {user.email} (Team ID: {user.team})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Users;
