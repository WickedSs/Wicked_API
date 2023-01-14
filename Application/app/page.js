'use client';

import Head from 'next/head'
import Image from 'next/image'
import { useRouter } from 'next/navigation'
import { useEffect, useState } from 'react'
import { setCookie, getCookie } from 'cookies-next'


import '../styles/dashboard.css'
import constant from '../constants';
import API_CALLS from './api/api_routes';
import Sellings from './scenes/sellings';
import Products from './scenes/products';
import Expenses from './scenes/expenses';
import Invoices from './scenes/invoices';
import Settings from './scenes/settings';
import Loading from '../components/loading';
import styles from '../styles/Home.module.css'
import Navigation from '../components/navigation_bar'



export default function Home() {
  
  const [selectedScene, setSelectedScene] = useState(0);
  const [currentTradeRegistry, setCurrentTradeRegistry] = useState(1);
  const [authenticated, setAuthenticated] = useState(undefined);
  const [token, setToken] = useState(undefined);
  
  const router = useRouter();
  const scenes = [
      { index : 0, scene: <Sellings _currentTradeRegistry={currentTradeRegistry} />, role: "Admin, Employee", scope: "Basic" },
      { index : 1, scene: <Products />, role: "Admin, Employee", scope: "Basic" },
      { index : 2, scene: <Expenses />, role: "Admin, Employee", scope: "Basic"  },
      { index : 3, scene: <Invoices _currentTradeRegistry={currentTradeRegistry} />, role: "Admin, Employee", scope: "Basic"  },
      { index : 4, scene: <Settings />, role: "Admin", scope: "Basic"  },
  ];  

  useEffect(() => {
    const check_access_token = async () => {
      const _token = window.localStorage.getItem("token");
      const response = await API_CALLS.isAuthenticated(_token);
      console.log(response);
      if (response.status_code == 200 && _token.length > 0) {
        setAuthenticated(true);
        setToken(constant.parseJwt(_token));
      } else if (response.status_code == 201) {
        setAuthenticated(true);
        window.localStorage.setItem("token", response.access_token);
        setToken(constant.parseJwt(response.access_token));
      } else {
        setAuthenticated(false);
        window.localStorage.removeItem("token")
        router.push("/account");
      }
    }
    check_access_token();
  }, []);
  
  return ( authenticated ? (
    <div className={styles.container}>
      <Head>
        <title>Upgrade</title>
        <meta name="description" content="Upgrade Application" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="dashboard">
        {/* <div>{token}</div> */}
        <Navigation _selectScene={{ selectedScene, setSelectedScene }} _tradeRegistry={{ currentTradeRegistry, setCurrentTradeRegistry }} token={token} />
        { scenes[selectedScene].role.split(",").includes(token.role) && token.scope === scenes[selectedScene].scope ? scenes[selectedScene].scene : null }
      </div>

    </div> ) : ( <Loading /> )
  )
}
