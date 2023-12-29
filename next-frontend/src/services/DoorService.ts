export function getDoorState() {
  return fetch("http://localhost:3000/api/v1/door")
}
