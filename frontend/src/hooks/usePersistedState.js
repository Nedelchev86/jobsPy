import {useState} from "react";

export const usePersistedState = (key, defaultValue) => {
    const [state, setState] = useState(() => {
        const persistedState = localStorage.getItem(key);

        if (persistedState) {
            return persistedState;
        }
        return defaultValue;
    });

    const setPersistedState = (value) => {
        setState(value);
        let serializedValue;
        if (typeof value === "function") {
            serializedValue = JSON.stringify(value(state));
        } else if (typeof value === "object") {
            serializedValue = JSON.stringify(value);
        } else {
            serializedValue = value;
        }

        localStorage.setItem(key, serializedValue);
    };
    return [state, setPersistedState];
};
