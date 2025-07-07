# Anveshak Bot Frontend

This is the frontend component of the Anveshak Bot project, which serves as an AI-powered help bot for the MOSDAC portal. The frontend is built using React and TailwindCSS, providing a user-friendly interface for interacting with the bot.

## Project Structure

- **src/**: Contains the source code for the frontend application.
  - **components/**: Contains React components for the chatbot interface.
    - `Chatbot.jsx`: Main component for handling user interactions.
    - `Message.jsx`: Component for displaying individual messages.
  - `App.jsx`: Main application component that integrates all components.
  - `index.js`: Entry point for the React application.
  - **styles/**: Contains styles for the application.
    - `tailwind.css`: Tailwind CSS styles.
- **public/**: Contains public assets.
  - `index.html`: Main HTML file for the frontend application.
- `package.json`: Lists dependencies and scripts for the frontend application.
- `tailwind.config.js`: Configuration file for Tailwind CSS.
- `README.md`: Documentation for setting up and running the frontend.

## Getting Started

To get started with the frontend, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd anveshak-bot/frontend
   ```

2. **Install Dependencies**:
   Make sure you have Node.js installed. Then run:
   ```bash
   npm install
   ```

3. **Run the Application**:
   Start the development server:
   ```bash
   npm start
   ```

4. **Open in Browser**:
   Navigate to `http://localhost:3000` in your web browser to view the application.

## Deployment

To deploy the frontend application, you can use platforms like Netlify or Vercel. Follow the respective platform's instructions for deploying a React application.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.