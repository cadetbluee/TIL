import "./App.css";
import Nav from "./components/Nav.jsx";
import Header from "./components/Header.jsx";
import Article from "./components/Article.jsx";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Contact from "./components/Contact.jsx";
import { ThemeProvider, createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: { main: "#5F9EA0" },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Container fixed className="App">
        <Nav></Nav>
        <Header></Header>
        <Grid container>
          <Grid item>
            <Article></Article>
          </Grid>
          <Grid item xs="12">
            <Contact></Contact>
          </Grid>
        </Grid>
      </Container>
    </ThemeProvider>
  );
}

export default App;
