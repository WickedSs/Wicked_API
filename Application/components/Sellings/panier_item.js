import Image from 'next/image'
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash, faMinus, faPlus, faArrowsUpDown, faHeart } from "@fortawesome/free-solid-svg-icons";
import { useEffect, useState } from 'react';

import defaultPng from '../../images/default.png'
import constant from '../../constants';


export default function PanierItem({ item, _onDelete, _onAlterQuantity, _onAlterColor, _onAlterSize }) {

    const [isSaved, setIsSaved] = useState(item.isSaved);

    return (
        <div className="panier_item">
            <div className='panier_image'>
                <Image src={defaultPng} width={128} height={128} objectFit='fit' />
            </div>
            <div className="panier_infos">
                <div className='item_name'>
                    <div>
                        {item.product_name}
                    </div>
                    <div>
                        {constant.formatter(item.price * item.currentQuantity)}
                    </div>
                </div>
                <div className='item_price'>
                    <div>
                        {constant.formatter(item.price)}
                    </div>
                    {
                        item.barcode ? (
                            <div style={{ color: item.quantity > 0 ? "#2a9d8f" : "#ff595e" }}>
                                {item.quantity > 0 ? "In Stock" : "Out Of Stock"}
                            </div>
                        ) : (<div></div>)
                    }
                    
                </div>
                <div className='item_size_stock_quantity'>
                    <div className='item_left_side'>
                        {
                            item.item_size && (
                            <div className='show size' onClick={() => _onAlterSize(item.id)}>
                                <div className='field'>
                                    <div className='selected'>{item.sizes}</div>
                                    <FontAwesomeIcon icon={faArrowsUpDown} style={{ fontSize: 16, color: "#fff" }} />
                                </div>
                            </div> )
                        }
                        {
                            item.item_model && (
                                <div className='show color' onClick={() => _onAlterColor(item.id)}>
                                    <div className='field'>
                                        <div className='selected'>{item.colors}</div>
                                        <FontAwesomeIcon icon={faArrowsUpDown} style={{ fontSize: 16, color: "#fff" }} />
                                    </div>
                                </div>
                            )
                        }
                        <div className='show quantity'>
                            <div onClick={() => _onAlterQuantity(item.id, -1) }>
                                <FontAwesomeIcon icon={faMinus} style={{ fontSize: 16, color: "#fff" }} />
                            </div>
                            <div className='selected' style={{ textAlign: 'center' }}>{ item.currentQuantity }</div>
                            <div onClick={() => _onAlterQuantity(item.id, 1) }>
                                <FontAwesomeIcon icon={faPlus} style={{ fontSize: 16, color: "#fff" }} />
                            </div>
                        </div>
                    </div>
                    <div className='item_right_side'>
                        {/* <div className='icon_button favourite' onClick={() => _saveItem(item.index)}>
                            <FontAwesomeIcon icon={faHeart} style={{ fontSize: 16, color: isSaved ? "#ff595e" : "#fff" }} />
                            <div>Save</div>
                        </div> */}
                        <div className='icon_button delete' onClick={() => _onDelete(item.id)}>
                            <FontAwesomeIcon icon={faTrash} style={{ fontSize: 16, color: "#fff" }} />
                            <div>Delete</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}