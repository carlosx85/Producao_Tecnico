mkdir -p ~/.streamilt/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~\.streamilt/config.toml