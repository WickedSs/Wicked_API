import Image from 'next/image'
import { createRef, useState } from 'react'
import { useRouter } from 'next/navigation'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRightFromBracket, faChevronUp, faChevronDown } from "@fortawesome/free-solid-svg-icons";



import constant from '../constants'
import '../styles/navigation_bar.css'
import API_CALLS from '../app/api/api_routes'
import defaultPng from '../images/default.png'


function NavigationTab({ _tab, _scene, _onClick }) {

    const { selectedScene, setSelectedScene } = _scene;
    const is_selected = selectedScene == _tab.index;

    return (
        <div className="tab" onClick={() => _onClick(_tab.index, _tab.title)}>
            <div className='tab_icon'>
                <FontAwesomeIcon icon={_tab.icon} style={{ fontSize: 20, color: is_selected ? "#fff" : "#777" }} />
            </div>
            <div className='tab_name' style={{ fontSize: 20, color: is_selected ? "#fff" : "#777" }}>
                {_tab.title}
            </div>
        </div>
    )
}

export default function Navigation({ _selectScene, _tradeRegistry, token }) {

    const tabRef = createRef();
    const router = useRouter();

    const _onRegistryClick = () => {
        let current = _tradeRegistry.currentTradeRegistry;
        current += 1;
        if (current >= constant.registries.length) {
            current = 0;
        }
        _tradeRegistry.setCurrentTradeRegistry(current);
    }

    const _changeTab = (tab, active) => {
        _selectScene.setSelectedScene(tab);
        tabRef.current.className = "selected_tab " + active;
    }

    const _logout = async () => {
        window.localStorage.removeItem("token");
        const response = await API_CALLS.logout();
        router.push("/account");
    }

    return (
        <div className="navigation_container">
            <div className='top'>
                <div className='logo'>
                    <div className='icon'>
                        <Image alt='profile picture' src={defaultPng} objectFit='contain'/>
                    </div>
                    <div className='names'>
                        <div className='title'>Root</div>
                        <div className='sub-title'>Administrator</div>
                    </div>
                </div>
                
                <div className='tabs_container'>
                    <div className='trade_registry'>
                        <div className='selected' onClick={(e) => _onRegistryClick()}>
                            <div className='value'>{constant.registries[_tradeRegistry.currentTradeRegistry]}</div>
                            <div className='chevrons'>
                                <FontAwesomeIcon icon={faChevronUp} style={{ fontSize: 12, color: "#fff" }} />
                                <FontAwesomeIcon icon={faChevronDown} style={{ fontSize: 12, color: "#fff" }} />
                            </div>
                        </div>
                    </div>
                    <div className='tabs'>
                        <div className="selected_tab Sellings" ref={tabRef}></div>
                        { 
                            constant.tabs.map((tab, index) => {
                                if (tab.role.split(",").includes(token.role) && tab.scope == token.scope) {
                                    return <NavigationTab key={index} _tab={tab} _scene={_selectScene} _onClick={_changeTab} />
                                }
                            })
                        }
                    </div>
                </div>
            </div>

            

            <div className='bottom'>
                <div className='exit' onClick={() => _logout()}>
                    <div className='icon_exit'>
                        <FontAwesomeIcon icon={faArrowRightFromBracket} style={{ fontSize: 24, color: "#fff" }} />
                    </div>
                    <div className='names'>
                        <div className='title'>LOG OUT</div>
                    </div>
                </div>
            </div>

        </div>
    )
}

