import React from "react";
import CalculatorHead from "../CalculatorHead/CalculatorHead";
import CalculatorBody from "../CalculatorBody/CalculatorBody";
import "./Calculator.css";
import { useState, useEffect } from "react";

const Calculator = (props) => {

    const [data, setData] = useState('');

    useEffect(() => {
        if (props.result) {
            setData([props.result])
        }
    }, [props.result])

    const bodyToHead = (childdata) => {
        setData([...childdata])
    }

    return (
        <div className="calculator">
            <CalculatorHead data={data}></CalculatorHead>
            <CalculatorBody bodyToHead={bodyToHead} postEquation={props.postEquation}></CalculatorBody>
        </div>
    )
}

export default Calculator;