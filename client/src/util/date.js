import { parse, formatDistanceToNow } from "date-fns";

const toIso = (date) => {
    return date.split(", ")[1].replace(" GMT", "");
};

const fromNow = (date) => {
    return formatDistanceToNow(
        parse(toIso(date), "dd MMM yyyy HH:mm:ss", new Date())
    );
};

export { fromNow, toIso };
