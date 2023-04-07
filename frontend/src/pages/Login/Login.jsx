import React, { useState } from "react";
import "./login.css";
import { useNavigate } from "react-router";
import request from "../../config";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    const data = {
      email,
      password,
    };
    request({
      method: "post",
      url: "/login",
      data,
    })
      .then((response) => {
        console.log(response);
        localStorage.setItem("token", data.token);
        localStorage.setItem("user", JSON.stringify(response.user));
        // console.log(data);
        navigate("/shop");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="form">
      <div className="form-body">
        <h3 className="header">Login</h3>
        <div className="input">
          <input
            type="email"
            id="email"
            className="form__input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email"
          />
        </div>
        <div className="input">
          <input
            className="form__input"
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </div>
      </div>
      <div className="footer">
        <button onClick={() => handleSubmit()} type="submit" className="btn">
          Login
        </button>
      </div>
    </div>
  );
};

export default Login;
