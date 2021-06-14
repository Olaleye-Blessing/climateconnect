import { Box, Button, makeStyles, Typography, withTheme } from "@material-ui/core";
import React, { useContext } from "react";

import { getLocalePrefix } from "../../../public/lib/apiOperations";
import getTexts from "../../../public/texts/texts";
import UserContext from "../context/UserContext";
import theme from "../../themes/theme";
// import SelectField from "./../general/SelectField";

const useStyles = makeStyles((theme) => {
  return {
    // TODO: fix "floating" state on top of the
    // background image. Need to tradeoff between responsiveness
    // and fixed "sticker" nature
    welcomeBanner: {
      backgroundColor: theme.palette.primary.main,
      minWidth: 300,
      borderRadius: 5,
      border: theme.borders.thick,
      color: "white",
      //   position: "absolute",
      position: "relative",
      //   position: fixed;
      // min-width: 100px;
      maxWidth: "800px",
      // z-index: 100;

      margin: "auto",
    },
    profileInner: {
      float: "left",
      position: "absolute",
      left: "0px",
      top: "0px",
      "z-index": " 1000",
      // background-color:" #92AD40",
      padding: "5px",
    },
    root: {
      marginBottom: theme.spacing(1.5),
      borderLeft: `5px solid ${theme.palette.primary.main}`,
    },

    userImage: {
      // Thin gray border
      // TODO(design): what color should this actually be -- I
      // don't see it represented in the XD mockup? Ideally
      // it'd be from our emerging design system
      border: theme.borders.thin,
      borderRadius: "50%",
      height: "45px",
      width: "45px",
      background: "white",
    },
    subsection: {
      // TODO(design): again want to make sure we reflect this color
      // scheme in our design system or in code. I just grabbed
      // this color from the color picker in Chrome DevTools
      background: "#f0f2f5",
      borderRadius: 4,
      padding: theme.spacing(1),
    },

    // TODO(Chris): is there a standard
    // set of Typography headings, components?
    headingText: {
      fontWeight: "bold",
    },

    welcomeMessage: {
      background: "white",
      borderRadius: "25px",
      color: theme.palette.secondary.main,
      display: "flex",
      alignItems: "center",
      width: "100%",
      // TODO: not sure about correct weight here
      fontWeight: "700",
      // padding: theme.spacing(1),
      padding: theme.spacing(1.5),
    },

    welcomeSubsection: {
      display: "flex",
    },

    hubName: {
      color: theme.palette.yellow.main,
    },

    buttonContainer: {
      display: "flex",
      justifyContent: "space-around",
    },
  };
});

const UserImage = () => {
  const classes = useStyles();
  return (
    <div className={`${classes.userImage}`}>
      {/* TODO: fetch correct user profile image here */}
      {/* Generic profile image if user is not logged in */}
      {/* <img /> */}
    </div>
  );
};

// TODO(Piper): generalize this spacing unit to be used in other places,
// for consistency.
const HorizontalSpacing = ({ children, size }) => {
  return (
    <Box css={{ marginTop: theme.spacing(size), marginBottom: theme.spacing(size) }}>
      {children}
    </Box>
  );
};

export default function Dashboard({ className }) {
  const classes = useStyles();
  const { user, locale } = useContext(UserContext);
  const texts = getTexts({ page: "general", locale: locale });

  return (
    <div className={`${classes.welcomeBanner}`}>
      <HorizontalSpacing size={1}>
        <Typography variant="h4" component="h1" className={`${classes.headingText}`}>
          {/* TODO: fix welcome messaging here */}
          Welcome to <span className={classes.hubName}>Test Hub</span>
        </Typography>
      </HorizontalSpacing>

      <div className={`${classes.subsection}`}>
        <HorizontalSpacing size={1}>
          <div className={`${classes.welcomeSubsection}`}>
            <UserImage />
            {/* TODO: doing some left spacing here -- trying to keep spacing directly out of the UI components, and isolated within Box components directly  */}
            <Box css={{ marginLeft: theme.spacing(1), width: "100%" }}>
              <div className={`${classes.welcomeMessage}`}>
                <Typography style={{ fontWeight: "600" }}>
                  This is standard user blurb text.
                </Typography>
              </div>
            </Box>
          </div>
        </HorizontalSpacing>

        <hr />

        <div className={`${classes.buttonContainer}`}>
          {/* When the user is logged out, we want to prompt them to sign up! And we don't
          show them the other controls. */}
          {!user ? (
            <>
              {/* TODO: are there already pre-existing buttons with icons for these? */}
              {/* TODO: replace buttons with Selects to indicate multiple actions */}
              <Button type="submit">Idee</Button>
              <Button type="submit">Project</Button>
              <Button type="submit">Organization</Button>
              {/* TODO: fix all links here */}
              <Button type="submit" href={"/profiles/"}>
                Profile
              </Button>
              <Button type="submit">Climate Match</Button>
            </>
          ) : (
            <>
              {/* TODO: fix sign up link */}
              <Button
                color="primary"
                component="div"
                href={getLocalePrefix(locale) + "/signup"}
                variant="contained"
              >
                {texts.join_now}
              </Button>
            </>
          )}
        </div>
      </div>
    </div>
  );
}
