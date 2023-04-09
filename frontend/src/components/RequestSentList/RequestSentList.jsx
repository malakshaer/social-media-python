import React, { useState, useEffect } from "react";
import User from "../User/User";
import "./requestsentlist.css";
import axios from "axios";
import Empty from "../Empty/Empty";

const RequestSendList = () => {
  const [sentToUsers, setSentToUsers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get("/get-sent-requests");
        const sentRequestList = response.data.requestList.map((user) => {
          const base64Image = `data:image/jpg;base64,${user.image}`;
          return {
            id: user.id,
            name: user.name,
            image: base64Image,
          };
        });
        setSentToUsers(sentRequestList);
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, []);

  const handleDeleteRequest = async (userId) => {
    try {
      await axios.delete(`/delete-request/${userId}`);
      setSentToUsers((prevUsers) =>
        prevUsers.filter((user) => user.id !== userId)
      );
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="users-card">
      {sentToUsers.length === 0 ? (
        <Empty />
      ) : (
        sentToUsers.map((user) => (
          <User
            key={user.id}
            name={user.name}
            image={user.image}
            textButton="delete request"
            onClick={() => handleDeleteRequest(user.id)}
          />
        ))
      )}
    </div>
  );
};

export default RequestSendList;
