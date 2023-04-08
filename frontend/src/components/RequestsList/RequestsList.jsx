import React, { useState, useEffect } from "react";
import User from "../User/User";
import "./requestslist.css";
import axios from "axios";
import Empty from "../Empty/Empty";

const RequestsList = () => {
  const [requestsWaiting, setRequestsWaiting] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await axios.get("/get-request-list");
        console.log(response);
        const requestList = response.data.requestList.map((request) => {
          return {
            id: request.id,
            name: request.name,
          };
        });
        setRequestsWaiting(requestList);
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, []);

  const handleAcceptUser = async (userId) => {
    try {
      await axios.post(`/accept/${userId}`);
      setRequestsWaiting((prevUsers) =>
        prevUsers.filter((user) => user.id !== userId)
      );
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div className="users-card">
      {requestsWaiting.length === 0 ? (
        <Empty />
      ) : (
        requestsWaiting.map((user) => (
          <User
            key={user.id}
            name={user.name}
            textButton="Accept"
            onClick={() => handleAcceptUser(user.id)}
          />
        ))
      )}
    </div>
  );
};

export default RequestsList;
