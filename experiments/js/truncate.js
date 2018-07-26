function truncateString(str, num) {
  // Clear out that junk in your trunk
  return str.slice(0, num) + '...';
}

console.log(truncateString('A-tisket a-tasket A green and yellow basket', 8));
