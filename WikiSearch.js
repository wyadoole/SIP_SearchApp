import React from "react";
import { TextField, Button } from "@material-ui/core";
import wikiSearchStyles from "./WikiSearchStyle";

const WikiSearch = () =>{
    const styles = wikiSearchStyles();

    return (
        <div className={styles.container}>
            <TextField id="wiki_search" label="Search Wikipedia" variant="filled"/>
            <Button variant="contained"color="primary">Search</Button>
        </div>
    )

};

export default WikiSearch;
