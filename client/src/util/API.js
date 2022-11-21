import store from "../store";
const baseUrl = import.meta.env.PROD ? "/api" : "http://localhost:5000/api";
console.log(baseUrl);

export default class API {
    static request(method, url, formData, auth = true) {
        let headers = {};
        if (auth) {
            const token = store.state.user?.token;
            headers["Authorization"] = `Bearer ${token}`;
        }

        const parse = (response, successCallback, failureCallback) => {
            response
                .json()
                .then((data) => {
                    // Set the message if the response has one
                    if (data.message) {
                        store.commit("setMessage", data.message);
                    }
                    successCallback(data);
                })
                .catch((error) => {
                    // Error parsing JSON
                    store.commit("setMessage", "An error has occurred.");
                    console.log("JSON parse error.");
                    failureCallback(error);
                });
        };

        return new Promise((resolve, reject) => {
            fetch(`${baseUrl}/${url}`, {
                method,
                headers,
                body: formData ?? null,
            })
                .then((response) => {
                    if (response.ok) {
                        parse(response, resolve, reject);
                    } else if (response.status === 401) {
                        store.dispatch("logout");
                        parse(response, resolve, reject);
                    } else {
                        parse(response, reject, reject);
                    }
                })
                .catch((error) => {
                    store.commit(
                        "setMessage",
                        error.message ?? "An error has occurred."
                    );
                    console.log("Network error.");
                    reject(error);
                });
        });
    }

    static get(url, auth) {
        return this.request("GET", url, null, auth);
    }
    static post(url, formData, auth) {
        return this.request("POST", url, formData, auth);
    }
    static put(url, formData, auth) {
        return this.request("PUT", url, formData, auth);
    }
    static delete(url, auth) {
        return this.request("DELETE", url, null, auth);
    }
}
