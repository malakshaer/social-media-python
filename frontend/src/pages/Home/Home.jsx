import React, { useEffect, useState } from "react";
import "./home.css";
import Navbar from "../../components/Navbar/Navbar";
import UserCard from "../../components/UserCard/UserCard";
import axios from "axios";

const Home = () => {
  const [users, setUsers] = useState([]);
  const [currentUser, setCurrentUser] = useState(null);

  useEffect(() => {
    async function fetchCurrentUser() {
      const response = await axios.get("get-user-info");
      setCurrentUser(response.data.id);
    }
    fetchCurrentUser();

    async function fetchUsers() {
      const response = await axios.get("get-all-users");
      setUsers(response.data);
    }
    fetchUsers();
  }, []);

  const filteredUsers = users.filter((user) => user._id !== currentUser);

  return (
    <div className="home">
      <Navbar />
      <div className="users-card">
        {filteredUsers.map((user) => (
          <UserCard key={user._id} data={user} />
        ))}
      </div>
    </div>
  );
};

export default Home;
