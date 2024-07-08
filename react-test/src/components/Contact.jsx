import React, { Component } from "react";
import Button from "@mui/material/Button";
import ButtonGroup from "@mui/material/ButtonGroup";
import {
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
} from "@mui/material";
import MailIcon from "@mui/icons-material/Mail";
export default class Contact extends Component {
  constructor(props) {
    super(props);
    this.state = {
      open: false,
    };
  }

  handleClickOpen = () => {
    this.setState({ open: true });
  };

  handleClose = () => {
    this.setState({ open: false });
  };

  render() {
    return (
      <article>
        <h2>
          <MailIcon />
          Contact Me
        </h2>
        <p>Feel free to contact me</p>
        <ButtonGroup>
          <Button variant="contained" onClick={this.handleClickOpen}>
            Create
          </Button>
          <Button variant="contained">Update</Button>
        </ButtonGroup>
        <Button variant="outlined" color="error">
          Delete
        </Button>
        <Dialog open={this.state.open} onClose={this.handleClose}>
          <DialogTitle>Title</DialogTitle>
          <DialogContent>
            <form>
                <label htmlFor="title"></label>
              <input type="text" name="title" />
                <label htmlFor="body"></label>
              <textarea name="body" id=""></textarea>

            </form>
          </DialogContent>
          <DialogActions>
            <Button variant="outlined">CREATE</Button>
            <Button variant="outlined" onClick={this.handleClose}>
              CANCEL
            </Button>
          </DialogActions>
        </Dialog>
      </article>
    );
  }
}
