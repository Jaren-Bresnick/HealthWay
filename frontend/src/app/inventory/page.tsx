'use client'

import { Button, Table } from "@mui/joy"
import IconButton from '@mui/joy/IconButton';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import DeleteIcon from '@mui/icons-material/Delete';
import { useEffect, useState } from "react";
import FormControl from '@mui/joy/FormControl';
import FormLabel from '@mui/joy/FormLabel';
import Input from '@mui/joy/Input';
import Modal from '@mui/joy/Modal';
import ModalDialog from '@mui/joy/ModalDialog';
import DialogTitle from '@mui/joy/DialogTitle';
import DialogContent from '@mui/joy/DialogContent';
import Stack from '@mui/joy/Stack';

function createData(
  name: string,
  quantity: number,
) {
  return { name, quantity };
}

export default function Home() {

  const [data, setData] = useState(null);
  const [openAddItemModal, setOpenAddItemModal] = useState(false);
  const [openReceiptModal, setOpenReceiptModal] = useState(false);
  const [openPantryModal, setOpenPantryModal] = useState(false);


  useEffect(() => {
    fetch('http://127.0.0.1:8000/inventory/get/abc')
      .then(response => response.json())
      .then(data => {
        let toAdd = []
        for (let item of data) {
          toAdd.push(createData(item[0], item[1]))
        }
        setData(toAdd);
      });
  }, []);

  const increaseQuantity = (index: number) => {
    const newData = [...data];
    const newQuantity = data[index].quantity + 1;
    newData[index].quantity += 1;
    setData(newData);

    const requestOptions = {
      method: "PUT",
    };

    fetch(`http://127.0.0.1:8000/inventory/update_quantity/abc/${data[index].name}/${newQuantity}`, requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.error(error));
  }

  const decreaseQuantity = (index: number) => {
    if (data[index].quantity <= 1) {
      return
    }
    const newData = [...data];
    const newQuantity = data[index].quantity - 1;
    newData[index].quantity -= 1;
    setData(newData);

    const requestOptions = {
      method: "PUT",
    };

    fetch(`http://127.0.0.1:8000/inventory/update_quantity/abc/${data[index].name}/${newQuantity}`, requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.error(error));
  }

  const deleteItem = (index: number) => {
    const newData = [...data];
    newData.splice(index, 1);
    setData(newData);

    const requestOptions = {
      method: "DELETE",
    };

    fetch(`http://127.0.0.1:8000/inventory/remove/${data[index].name}/abc`, requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.error(error));
  }

  const addItem = (name: string, quantity: number) => {
    const newData = [...data];
    newData.push(createData(name, quantity));
    setData(newData);

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
      "product": name,
      "quantity": quantity,
      "userid": "abc"
    });

    const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
    };

    fetch("http://127.0.0.1:8000/inventory/add_item", requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.error(error));
  }

  return (
    <div className='flex flex-row justify-center'>

      <div className='m-10 flex flex-col space-y-4 max-w-[1100px]'>

        <div className='flex flex-col'>
          <p className='font-bold text-2xl'>Your Inventory</p>
          <p className='text-slate-500'>Here are a list of everything Food Inventory has classified for you so far. If you see any errors, you can edit the quantity, delete items, or add items. You can use this list as an inspiration when comoing up with recipies, or to reference when grocery shopping to see what you already have at home.</p>
        </div>

        <Table>
          <thead>
            <tr>
              <th>Row</th>
              <th>Ingredient</th>
              <th>Quantity</th>
            </tr>
          </thead>
          <tbody>
            {data && data.map((row, idx) => (
              <tr key={idx}>
                <td>
                  <p className='text-lg font-semibold'>
                    {idx + 1}
                  </p>
                </td>
                <td>
                  <p className='text-lg font-semibold'>
                    {row.name}
                  </p>
                </td>
                <td>

                  <div className='grid grid-cols-4 gap-2'>
                    <IconButton variant="outlined" size="sm" onClick={() => decreaseQuantity(idx)}>
                      <RemoveIcon />
                    </IconButton>
                    <p className='text-lg font-semibold text-center'>
                      {row.quantity}
                    </p>
                    <IconButton variant="outlined" size="sm" onClick={() => increaseQuantity(idx)}>
                      <AddIcon />
                    </IconButton>
                    <IconButton variant="outlined" color='danger' size="sm" onClick={() => deleteItem(idx)}>
                      <DeleteIcon />
                    </IconButton>
                  </div>

                </td>
              </tr>
            ))}
          </tbody>
        </Table>

        <Button color="neutral" variant="outlined" onClick={() => setOpenAddItemModal(true)}>
          Add Item
        </Button>

        <div className='grid grid-cols-2 gap-4'>
          <Button color="neutral" variant="outlined" onClick={() => setOpenReceiptModal(true)}>
            Scan Receipt
          </Button>

          <Button color="neutral" variant="outlined" onClick={() => setOpenPantryModal(true)}>
            Scan Pantries
          </Button>

        </div>

      </div>

      <Modal open={openAddItemModal} onClose={() => setOpenAddItemModal(false)}>
        <ModalDialog>
          <DialogTitle>Add New Itme</DialogTitle>
          <DialogContent>Fill in the the product name and quantity</DialogContent>
          <form
            onSubmit={(event: React.FormEvent<HTMLFormElement>) => {
              event.preventDefault();
              const quantity = parseInt(event.currentTarget[1].value)
              if (isNaN(quantity)) {
                alert("Quantity must be a number");
                return;
              }
              addItem(event.currentTarget[0].value, quantity);
              setOpenAddItemModal(false);
            }}
          >
            <Stack spacing={2}>
              <FormControl>
                <FormLabel>Product Name</FormLabel>
                <Input autoFocus required />
              </FormControl>
              <FormControl>
                <FormLabel>Quantity</FormLabel>
                <Input required />
              </FormControl>
              <Button type="submit" variant="outlined" color="neutral">Submit</Button>
            </Stack>
          </form>
        </ModalDialog>
      </Modal>

    </div>
  );
}
