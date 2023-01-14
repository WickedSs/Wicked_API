import Image from "next/image"
import constant from "../../constants";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash, faEdit } from "@fortawesome/free-solid-svg-icons";
import default_png from '../../images/default.png';


export default function ProductItem({ _item }) {
    return (
        <div className="product_item">
            <div className="product avatar">
                <Image  src={default_png} objectFit="contain" height={64} width={64} />
            </div>
            <div className="product pr_name_barode_category">
                <span>{_item.product_name}</span>
                <div className="pr_detail sub_details">
                    <span>{_item.barcode}</span>
                    <span></span>
                    <span>{_item.category}</span>
                </div>
            </div>
            <div className="product pr_bought">
                <span>Bought</span>
                <span style={{ color: "#FDC186" }} >{constant.formatter(_item.bought || 0)}</span>
            </div>
            <div className="product pr_price">
                <span>Price</span>
                <span style={{ color: "#06d6a0" }} >{constant.formatter(_item.price || 0)}</span>
            </div>
            <div className="product pr_link">
                <span>Market</span>
                <span style={{ color: "#4ea8de" }} >{constant.formatter(_item.market || 0)}</span>
            </div>
            <div className="product pr_quantity">
                <span>Quantity</span>
                <span style={{  }} >{_item.quantity}</span>
            </div>
            <div className="product pr_sold">
                <span>Sold</span>
                <span style={{  }} >{_item.sold}</span>
            </div>
            <div className="product pr_earned">
                <span>Earned</span>
                <span style={{  }} >{constant.formatter(_item.earned || 0)}</span>
            </div>
        </div>
    )
}