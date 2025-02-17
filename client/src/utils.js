export const getImageUrl = (path) => {
    return new URL("assets/"+path, import.meta.url).href;
};

export const getCSRFToken = () => {
    const csrfToken = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='));  // Replace 'csrf_token' with your actual cookie name
    return csrfToken ? csrfToken.split('=')[1] : null;
};