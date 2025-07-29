import { createContext, useContext, useState } from 'react';

const Context = createContext();

export function Provider({ children }) {
    const [displayName, setDisplayName] = useState("");
    const [email, setEmail] = useState("");
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [allProductSearchInput, setAllProductSearchInput] = useState("");

    return (
        <Context.Provider value={{
            displayName,
            setDisplayName,
            email,
            setEmail,
            isLoggedIn,
            setIsLoggedIn,
            allProductSearchInput,
            setAllProductSearchInput
        }}>
            {children}
        </Context.Provider>
    );
}

export function useProvider() {
    return useContext(Context);
}
