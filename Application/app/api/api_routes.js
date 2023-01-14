// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import axios from 'axios';



const construct_header = (bearer) => {
  return { "Authorization" : `Bearer ${bearer == null ? "" : bearer}` }
}


const loginUser = async (username, password) => {
  const res = await fetch("http://localhost:3105/api/user/access-token", {
    method: "POST",
    credentials: "include",
    headers: {
      "Content-Type" : "application/x-www-form-urlencoded;charset=UTF-8"
    },
    body: new URLSearchParams({
      username : username,
      password : password
    }),
  });
  const data = await res.json();
  return data;
};

const isAuthenticated = async (bearer) => {
  const res = await axios.post("http://localhost:3105/api/user/authorization", {
    withCredentials : "include",
    headers : construct_header(bearer)
  });
  const data = await res.json();
  return data;
};

const logout = async () => {
  const res = await fetch("http://localhost:3105/api/user/logout", {
    method: "POST",
    credentials: "include",
  });
  const data = await res.json();
  return data;
};

const SELECT = async (type, column=undefined, key=undefined, port=3100, host="localhost") => {
  const _column = (column !== undefined ? "_" + column : "");
  const _key = (key !== undefined ? "/" + key : "");
  const endpoint = "http://"+host+":"+port+"/api/" + type + _column + _key;
  try {
    const response = await axios.get(endpoint);
    return response;
  } catch (error) {
    console.log("Error SELECT " + type + ": ", error);
  }
};

const UPDATE = async (type, column=undefined, key=undefined, item, port=3100, host="localhost") => {
  const _column = (column !== undefined ? "_" + column : "");
  const _key = (key !== undefined ? "/" + key : "");
  const endpoint = "http://"+host+":"+port+"/api/" + type + _column + _key;
  try {
    const response = await axios.put(endpoint, item, {
      headers: { 'Content-Type': 'application/json' }, 
    });
    return response;
  } catch (error) {
    console.log("Error UPDATE " + type + ": ", error);
  }
};

const INSERT = async (type, column=undefined, key=undefined, items, port=3100, host="localhost") => {
  const _column = (column !== undefined ? "_" + column : "");
  const _key = (key !== undefined ? "/" + key : "");
  const endpoint = "http://"+host+":"+port+"/api/" + type + _column + _key;
  try {
    const response = await axios.post(endpoint, items, {
        headers: { 'Content-Type': 'application/json' }
      }, { withCredentials: true },
    );
    return response;
  } catch (error) {
    console.log("Error INSERT " + type + ": ", error);
  }
}

const DELETE = async (type, column=undefined, key=undefined, port=3100, host="localhost") => {
  const _column = (column !== undefined ? "_" + column : "");
  const _key = (key !== undefined ? "/" + key : "");
  const endpoint = "http://"+host+":"+port+"/api/" + type + _column + _key;
  try {
    const response = await axios.delete(endpoint);
    return response;
  } catch (error) {
    console.log("Error DELETE " + type + ": ", error);
  }
}

const REQUEST_FILE = async (type, column=undefined, key=undefined, filename="default", port=3100, host="localhost") => {
  const _column = (column !== undefined ? "_" + column : "");
  const endpoint = "http://"+host+":"+port+"/api/" + type + _column + "/?id=" + key + "&filename=" + filename;
  try {
    const response = await axios.get(endpoint);
    return response;
  } catch (error) {
    console.log("Error REQUEST_FILE " + type + ": ", error);
  }
}

const API_CALLS = { loginUser, SELECT, UPDATE, INSERT, DELETE, REQUEST_FILE, isAuthenticated, logout }
export default API_CALLS;
