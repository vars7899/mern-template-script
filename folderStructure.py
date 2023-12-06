folderStructure = {
    "app": {
        "server": {
            "server.js": """
const express = require("express");

const app = express();
const PORT = process.env.PORT | 5000;

app.get("/", (req, res) => res.status(200).json({ success: true, message: "Server is running." }))

app.listen(PORT, ()=>{
    console.log(`SUCCESS\t-->\t\tServer UP on PORT ${PORT}`)
})
            """,
            "cmd.yarn": "yarn init -y && yarn add express mongoose && yarn add -D nodemon",
            "app": {
                "models": {
                    "index.js": ""
                },
                "controllers": {
                    "index.js": ""
                },
                "routes": {
                    "index.js": ""
                },
                "functions": {
                    "index.js": ""
                },
                "config": {
                    "index.js": ""
                },
                "middleware": {
                    "index.js": ""
                },
                "constants": {
                    "index.js": ""
                },
                "templates": {
                    "index.js": ""
                },
            }
        },
        # << Init vite
        "cmd.yarn": "yarn create vite client --template react-ts",
        "readme.md": """
 _______ _______ ______ _______                                 
|   |   |    ___|   __ \    |  |                                
|       |    ___|      <       |                                
|_______|_______|______________|_____   _______ _______ _______ 
|_     _|    ___|   |   |   __ \     |_|   _   |_     _|    ___|
  |   | |    ___|       |    __/       |       | |   | |    ___|
  |___| |_______|__|_|__|___|  |_______|___|___| |___| |_______|
                                                                                                     
------------------------------------
NodeJS
Express
Mongoose
React (using vite react-ts template)
react-router-dom
------------------------------------
Created By Vaibhav Dhiman
github --> https://github.com/vars7899
        """
    }
}

clientFolderStructure = {
    # << Install dependencies
    "cmd.yarn": "yarn && yarn add react-router-dom",
    "components": {
            "index.ts": ""
        },
    "screens": {
            "index.ts": ""
        },
    "layouts": {
            "index.ts": ""
        },
    "redux": {
            "index.ts": ""
        },
    "navigation": {
            "index.ts": ""
        },
    "hooks": {
            "index.ts": ""
        },
    "functions": {
            "index.ts": ""
        },
    "assets": {
            "index.ts": ""
        }
}
