import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import request from "../../config";

const Logout = () => {
  const [show, setShow] = useState(false);
  const navigate = useNavigate();

  const Logout = async () => {
    const token = await localStorage.getItem("token");
    console.log("===>" + token);

    request({
      method: "post",
      url: "/register",
    })
      .then((response) => {
        setShow(true);
        localStorage.removeItem("token");
        window.alert("Successfully Logout");

        navigate("/login");
        window.location.reload();
      })
      .catch((error) => {
        console.log(error);
      });
  };

  useEffect(() => {
    const confirmBox = window.confirm("Do you really want to Logout?");
    if (confirmBox === true) {
      Logout();
      localStorage.removeItem("token");
      navigate("/login", { replace: true });
    } else {
      navigate("/");
    }
  });

  return (
    <div>
      <h1>{show ? "Logout Successfully!" : "processing..."}</h1>
    </div>
  );
};

export default Logout;
