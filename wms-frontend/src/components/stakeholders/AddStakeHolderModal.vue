<script setup lang="ts">
import { ref } from "vue";
import axios from '@/plugins/axios.js';

const emit = defineEmits(['instance-added']);
const visible = ref(false);

const formData = ref({
    name: '',
    address: '',
    mobile: '',
    email: '',
    company_name: '',
    type: '',
});
const typeOptions = ref([
    { name: 'Customer', value: 'Customer' },
    { name: 'Supplier', value: 'supplier' }
]);

const handleSubmit = async () => {
    try {
        const data = new FormData();
        data.append('name', formData.value.name);
        data.append('address', formData.value.address);
        data.append('mobile', formData.value.mobile);
        data.append('email', formData.value.email);
        data.append('company_name', formData.value.company_name);
        data.append('type', formData.value.type);

        const response = await axios.post('/api/accounts/stakeholders/', data);
        console.log(response);
        visible.value = false;
        emit('instance-added');
    } catch (error) {
        console.error('Creation failed:', error);
    }
};

</script>

<template>
    <div class="">
        <div class="flex justify-end">
            <Button label="Add" @click="visible = true" />
        </div>
        <Dialog v-model:visible="visible" modal header="Edit Profile" :style="{ width: '40rem' }">
            <span class="text-surface-500 dark:text-surface-400 block mb-8">Update your information.</span>
            <div class="flex items-center gap-4 mb-4">
                <label for="name" class="font-semibold w-24">Name</label>
                <InputText id="name" v-model=formData.name class="flex-auto" autocomplete="off" />
            </div>
            <div class="flex items-center gap-4 mb-4">
                <label for="address" class="font-semibold w-24">Address</label>
                <InputText id="address" v-model=formData.address class="flex-auto" autocomplete="off" />
            </div>
            <div class="flex items-center gap-4 mb-4">
                <label for="mobile" class="font-semibold w-24">Phone</label>
                <InputText id="mobile" v-model=formData.mobile class="flex-auto" autocomplete="off" />
            </div>
            <div class="flex items-center gap-4 mb-8">
                <label for="email" class="font-semibold w-24">Email</label>
                <InputText id="email" v-model=formData.email class="flex-auto" autocomplete="off" />
            </div>
            <div class="flex items-center gap-4 mb-8">
                <label for="type" class="font-semibold w-24">Type</label>
                <Select v-model=formData.type :options="typeOptions" optionLabel="name" optionValue="value"
                    placeholder="Select a Type" class="w-full md:w-14rem" />

            </div>
            <div class="flex items-center gap-4 mb-8">
                <label for="company_name" class="font-semibold w-24">Company Name</label>
                <InputText id="company_name" v-model=formData.company_name class="flex-auto" autocomplete="off" />
            </div>
            <div class="flex justify-end gap-2">
                <Button type="button" label="Cancel" severity="secondary" @click="visible = false"></Button>
                <Button type="submit" label="Save" @click="handleSubmit()"></Button>
            </div>
        </Dialog>
    </div>
</template>

<style></style>
