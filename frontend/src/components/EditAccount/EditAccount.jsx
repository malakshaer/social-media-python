import React, { useState } from "react";
import Navbar from "../Navbar/Navbar";
import "./editaccount.css";
import Button from "../Button/Button";
import request from "../../config";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChevronDown } from "@fortawesome/free-solid-svg-icons";
import axios from "axios";

const EditAccount = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [bio, setBio] = useState("");
  const [image, setImage] = useState("");
  const [error, setError] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [isExpandedEdit, setIsExpandedEdit] = useState(false);
  const [isExpandedPrivacy, setIsExpandedPrivacy] = useState(false);
  const [message, setMessage] = useState("");

  const handleUpdateAccount = async (e) => {
    e.preventDefault();
    if (!firstName || !lastName) {
      setError("First name and last name are required.");
      return;
    }

    let userData = { firstName, lastName, bio };
    if (image) {
      userData = { ...userData, image };
    }
    const token = localStorage.getItem("token");

    request({
      method: "put",
      url: "update-profile",
      data: userData,
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((data) => {
        console.log(data);
        setError(null);
        setSuccessMessage("Account updated successfully.");
        setTimeout(() => {
          setSuccessMessage(null);
        }, 5000);
      })
      .catch((error) => {
        console.log(error);
        setSuccessMessage(null);
        setError("Error updating account.");
        setTimeout(() => {
          setError(null);
        }, 5000);
      });
  };

  const handleButtonClick = async () => {
    try {
      const response = await axios.put(`/private`);
      console.log(response);
      setMessage(response.data.message);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <Navbar />
      <div className="edit-account">
        <div className="arrow">
          <h1 onClick={() => setIsExpandedEdit(!isExpandedEdit)}>
            Edit your account information
          </h1>
          <FontAwesomeIcon icon={faChevronDown} className="arrow-icon" />
        </div>
        {isExpandedEdit && (
          <form className="form-group">
            <label htmlFor="image">Profile Image: </label>
            <input
              type="file"
              name="image"
              id="image"
              onChange={(e) => {
                const file = e.target.files[0];
                const reader = new FileReader();
                reader.readAsDataURL(file);
                reader.onload = () => {
                  setImage(reader.result);
                };
              }}
            />
            <label htmlFor="firstName">First Name: </label>
            <input
              className="form-input"
              type="text"
              name="firstName"
              id="firstName"
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
            />
            <label htmlFor="lastName">Last Name: </label>
            <input
              type="text"
              name="lastName"
              id="lastName"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            />
            <label htmlFor="bio">Bio: </label>
            <textarea
              name="bio"
              id="bio"
              value={bio}
              onChange={(e) => setBio(e.target.value)}
            />
            <Button text={"save"} onClick={handleUpdateAccount} />
            {error && <p className="error">{error}</p>}
            {successMessage && (
              <div className="success-message">{successMessage}</div>
            )}
          </form>
        )}
        <div className="arrow">
          <h1 onClick={() => setIsExpandedPrivacy(!isExpandedPrivacy)}>
            Privacy settings
          </h1>
          <FontAwesomeIcon icon={faChevronDown} className="arrow-icon" />
        </div>
        {isExpandedPrivacy && (
          <div>
            <p className="privacy">{message}</p>
            <button onClick={handleButtonClick}>Change</button>
          </div>
        )}
      </div>
    </div>
  );
};

export default EditAccount;
