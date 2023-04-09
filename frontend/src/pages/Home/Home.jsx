import React, { useEffect, useState } from "react";
import "./home.css";
import Navbar from "../../components/Navbar/Navbar";
import UserCard from "../../components/UserCard/UserCard";
import axios from "axios";

const Home = () => {
  const [users, setUsers] = useState([]);
  const [currentUser, setCurrentUser] = useState(null);
  const [followingList, setFollowingList] = useState([]);
  const [requestedList, setRequestedList] = useState([]);

  useEffect(() => {
    async function fetchCurrentUser() {
      const response = await axios.get("get-user-info");
      setCurrentUser(response.data.id);
      setFollowingList(response.data.following_list);
      setRequestedList(response.data.requested_list);
    }
    fetchCurrentUser();

    async function fetchUsers() {
      const response = await axios.get("get-all-users");
      setUsers(response.data);
    }
    fetchUsers();
  }, []);

  const filteredUsers = users.filter(
    (user) =>
      user._id !== currentUser &&
      !followingList.some((u) => u.id === user._id) &&
      !requestedList.some((u) => u.id === user._id)
  );

  return (
    <div className="home">
      <Navbar />
      <div className="users-card">
        {filteredUsers.map((user) => (
          <UserCard
            key={user._id}
            data={user}
            firstName={user.firstName}
            lastName={user.lastName}
            numberFollowers={user.num_followers}
            numberFollowing={user.num_following}
            bio={user.bio}
            image={user.image}
          />
        ))}
      </div>
    </div>
  );
};

export default Home;
