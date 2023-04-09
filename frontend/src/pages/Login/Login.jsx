import React, { useState } from "react";
import "./login.css";
import { useNavigate } from "react-router";
import request from "../../config";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!email || !password) {
      setError("Please enter both email and password.");
      return;
    }
    const data = {
      email,
      password,
    };
    request({
      method: "post",
      url: "login",
      data,
    })
      .then((response) => {
        console.log(response);
        localStorage.setItem("token", response.token);
        localStorage.setItem("user", response.name);
        navigate("/home");
      })
      .catch((error) => {
        setError("Invalid email or password.");
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
        {error && <p className="error">{error}</p>}
      </div>
      <div className="footer">
        <button onClick={handleSubmit} type="submit">
          Login
        </button>
        <div>
          <p>
            Don't have an account <a href="/"> Register</a>{" "}
          </p>
        </div>
      </div>
    </div>
  );
};

export default Login;
