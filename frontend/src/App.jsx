import React, { useState } from 'react';
import Chatbot from './components/Chatbot';
import './styles/tailwind.css';

const App = () => {
    const [isLoading, setIsLoading] = useState(false);

    return (
        <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
            <h1 className="text-3xl font-bold mb-4">Anveshak - AI Help Bot</h1>
            {isLoading && <div className="loader">Loading...</div>}
            <Chatbot setIsLoading={setIsLoading} />
        </div>
    );
};

export default App;