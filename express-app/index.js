import cors from "cors";
import path from "path";
import consola from "consola";
import express from "express";
import bodyParser from "body-parser";

const app = express();

app.use(cors());
app.use(bodyParser.json());

const PORT = 3000;

app.get("/express", (req, res) => {
  return res.sendFile(path.join(__dirname, "./public/index.html"));
});

app.get("/express-api-1", (req, res) => {
  return res.status(200).json({
    message: "Hello from express api 1",
    success: true,
  });
});

app.get("/express-api-2", (req, res) => {
  return res.status(200).json({
    message: "Hello from express api 2",
    success: true,
  });
});

const startApp = () => {
  app.listen(PORT, () =>
    consola.success({
      message: `Server started on port ${PORT}`,
      badge: true,
    })
  );
};

startApp();
