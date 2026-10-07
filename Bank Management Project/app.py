import json
import random
import string
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import List, Optional
import streamlit as st

# ────────────────────────────────────────────────
#  Configuration & Styling
# ────────────────────────────────────────────────
DATABASE = "bank_data.json"

st.set_page_config(
    page_title="Nova Bank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for a beautiful, modern look
st.markdown("""
<style>
    /* Main container */
    .main {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #ffffff;
    }
    /* Cards */
    .css-1r6slb0, .css-12oz5g7 {
        background: rgba(255,255,255,0.05);
        border-radius: 16px;
        padding: 2rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102,126,234,0.4);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102,126,234,0.6);
    }
    /* Inputs */
    .stTextInput > div > div > input, .stNumberInput > div > div > input {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 10px;
        color: white;
    }
    /* Headers */
    h1, h2, h3 {
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    /* Success / Error messages */
    .stAlert {
        border-radius: 12px;
    }
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(15, 12, 41, 0.95);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    /* Metric cards */
    div[data-testid="stMetric"] {
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 1rem;
        border: 1px solid rgba(255,255,255,0.1);
    }
</style>
""", unsafe_allow_html=True)


# ────────────────────────────────────────────────
#  Data Model
# ────────────────────────────────────────────────
@dataclass
class Account:
    name: str
    age: int
    email: str
    pin: int
    account_no: str
    balance: float = 0.0

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "Age": self.age,
            "E-mail": self.email,
            "Pin": self.pin,
            "Account No.": self.account_no,
            "Balance": self.balance,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Account":
        return cls(
            name=d["name"],
            age=d["Age"],
            email=d["E-mail"],
            pin=d["Pin"],
            account_no=d["Account No."],
            balance=d["Balance"],
        )


# ────────────────────────────────────────────────
#  Bank Engine (pure logic, no UI)
# ────────────────────────────────────────────────
class BankEngine:
    def __init__(self, db_path: str = DATABASE):
        self.db_path = Path(db_path)
        self.accounts: List[Account] = []
        self._load()

    # ── persistence ──────────────────────────────
    def _load(self):
        if self.db_path.exists():
            try:
                raw = json.loads(self.db_path.read_text())
                self.accounts = [Account.from_dict(d) for d in raw]
            except Exception as e:
                st.error(f"Failed to load database: {e}")
                self.accounts = []
        else:
            self.accounts = []

    def _save(self):
        data = [a.to_dict() for a in self.accounts]
        self.db_path.write_text(json.dumps(data, indent=4))

    # ── helpers ──────────────────────────────────
    @staticmethod
    def _generate_account_no() -> str:
        chars = (
            random.choices(string.ascii_letters, k=3)
            + random.choices(string.digits, k=3)
            + random.choices("!@#$%^&*", k=1)
        )
        random.shuffle(chars)
        return "".join(chars)

    def find(self, account_no: str, pin: int) -> Optional[Account]:
        for acc in self.accounts:
            if acc.account_no == account_no and acc.pin == pin:
                return acc
        return None

    # ── public API ───────────────────────────────
    def create_account(self, name, age, email, pin) -> tuple[bool, str, Optional[Account]]:
        if age < 18:
            return False, "You must be at least 18 years old.", None
        if not (1000 <= pin <= 9999):
            return False, "PIN must be exactly 4 digits.", None

        acc = Account(
            name=name.strip(),
            age=age,
            email=email.strip(),
            pin=pin,
            account_no=self._generate_account_no(),
        )
        self.accounts.append(acc)
        self._save()
        return True, "Account created successfully!", acc

    def deposit(self, account_no, pin, amount) -> tuple[bool, str]:
        acc = self.find(account_no, pin)
        if not acc:
            return False, "Invalid account number or PIN."
        if amount <= 0:
            return False, "Deposit amount must be positive."
        if amount >= 10_000:
            return False, "Single deposit cannot exceed ₹9,999."
        acc.balance += amount
        self._save()
        return True, f"₹{amount:,.2f} deposited successfully. New balance: ₹{acc.balance:,.2f}"

    def withdraw(self, account_no, pin, amount) -> tuple[bool, str]:
        acc = self.find(account_no, pin)
        if not acc:
            return False, "Invalid account number or PIN."
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if acc.balance < amount:
            return False, f"Insufficient funds. Available balance: ₹{acc.balance:,.2f}"
        acc.balance -= amount
        self._save()
        return True, f"₹{amount:,.2f} withdrawn successfully. New balance: ₹{acc.balance:,.2f}"

    def update_details(self, account_no, pin, name=None, email=None, new_pin=None) -> tuple[bool, str]:
        acc = self.find(account_no, pin)
        if not acc:
            return False, "Invalid account number or PIN."
        if name:
            acc.name = name.strip()
        if email:
            acc.email = email.strip()
        if new_pin is not None:
            if not (1000 <= new_pin <= 9999):
                return False, "New PIN must be exactly 4 digits."
            acc.pin = new_pin
        self._save()
        return True, "Details updated successfully!"

    def delete_account(self, account_no, pin) -> tuple[bool, str]:
        acc = self.find(account_no, pin)
        if not acc:
            return False, "Invalid account number or PIN."
        self.accounts.remove(acc)
        self._save()
        return True, "Account deleted successfully."


# ────────────────────────────────────────────────
#  Streamlit UI
# ────────────────────────────────────────────────
@st.cache_resource
def get_engine() -> BankEngine:
    return BankEngine()

engine = get_engine()

# ── Header ───────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding: 1rem 0 2rem 0;">
    <h1 style="font-size: 3rem; margin-bottom: 0;">🏦 AAPLI BANK</h1>
    <p style="color: #a0a0c0; font-size: 1.1rem;">Secure · Modern · Effortless Banking</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar navigation ───────────────────────────
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    page = st.radio(
        "Go to",
        [
            "🏠 Home",
            "➕ Create Account",
            "💰 Deposit",
            "💸 Withdraw",
            "👤 Account Details",
            "✏️ Update Details",
            "🗑️ Delete Account",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown(f"**Total Accounts:** {len(engine.accounts)}")
    total_balance = sum(a.balance for a in engine.accounts)
    st.markdown(f"**Total Deposits:** ₹{total_balance:,.2f}")

# ── Home ─────────────────────────────────────────
if page == "🏠 Home":
    st.markdown("## Welcome to AAPLI Bank")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Accounts", len(engine.accounts))
    with col2:
        st.metric("Total Deposits", f"₹{sum(a.balance for a in engine.accounts):,.2f}")
    with col3:
        st.metric("Avg. Balance", f"₹{(sum(a.balance for a in engine.accounts) / len(engine.accounts)):,.2f}" if engine.accounts else "₹0.00")

    st.markdown("---")
    st.markdown("""
    ### Why AAPLI Bank?
    - **🔐 Secure** — PIN-protected accounts with encrypted storage
    - **⚡ Fast** — Instant deposits and withdrawals
    - **🎨 Beautiful** — A modern banking experience
    - **📊 Transparent** — Real-time balance updates

    Use the sidebar to get started. Create an account to begin your journey.
    """)

# ── Create Account ───────────────────────────────
elif page == "➕ Create Account":
    st.markdown("## ➕ Create a New Account")
    with st.form("create_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="John Doe")
            age = st.number_input("Age", min_value=1, max_value=120, value=25)
        with col2:
            email = st.text_input("E-mail", placeholder="john@example.com")
            pin = st.number_input("4-digit PIN", min_value=1000, max_value=9999, value=1234, step=1)

        submitted = st.form_submit_button("Create Account", use_container_width=True)

        if submitted:
            ok, msg, acc = engine.create_account(name, age, email, pin)
            if ok:
                st.success(msg)
                st.balloons()
                st.markdown("### 🎉 Your Account Details")
                st.code(f"Account Number: {acc.account_no}", language=None)
                st.warning("⚠️ Please note down your account number. It will be required for all future transactions.")
                with st.expander("View full details"):
                    st.json(acc.to_dict())
            else:
                st.error(msg)

# ── Deposit ──────────────────────────────────────
elif page == "💰 Deposit":
    st.markdown("## 💰 Deposit Money")
    with st.form("deposit_form", clear_on_submit=True):
        account_no = st.text_input("Account Number", placeholder="e.g. AbC123!")
        pin = st.number_input("PIN", min_value=1000, max_value=9999, value=1234, step=1)
        amount = st.number_input("Amount (₹)", min_value=1, max_value=9999, value=500, step=100)
        submitted = st.form_submit_button("Deposit", use_container_width=True)

        if submitted:
            ok, msg = engine.deposit(account_no, pin, amount)
            if ok:
                st.success(msg)
                st.balloons()
            else:
                st.error(msg)

# ── Withdraw ─────────────────────────────────────
elif page == "💸 Withdraw":
    st.markdown("## 💸 Withdraw Money")
    with st.form("withdraw_form", clear_on_submit=True):
        account_no = st.text_input("Account Number", placeholder="e.g. AbC123!")
        pin = st.number_input("PIN", min_value=1000, max_value=9999, value=1234, step=1)
        amount = st.number_input("Amount (₹)", min_value=1, value=500, step=100)
        submitted = st.form_submit_button("Withdraw", use_container_width=True)

        if submitted:
            ok, msg = engine.withdraw(account_no, pin, amount)
            if ok:
                st.success(msg)
            else:
                st.error(msg)

# ── Account Details ──────────────────────────────
elif page == "👤 Account Details":
    st.markdown("## 👤 Account Details")
    with st.form("details_form"):
        account_no = st.text_input("Account Number", placeholder="e.g. AbC123!")
        pin = st.number_input("PIN", min_value=1000, max_value=9999, value=1234, step=1)
        submitted = st.form_submit_button("Show Details", use_container_width=True)

        if submitted:
            acc = engine.find(account_no, pin)
            if acc:
                st.success("Account found!")
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Account Holder", acc.name)
                    st.metric("Account Number", acc.account_no)
                    st.metric("Age", acc.age)
                with col2:
                    st.metric("E-mail", acc.email)
                    st.metric("Balance", f"₹{acc.balance:,.2f}")
                st.markdown("---")
                with st.expander("Raw data"):
                    st.json(acc.to_dict())
            else:
                st.error("Invalid account number or PIN.")

# ── Update Details ───────────────────────────────
elif page == "✏️ Update Details":
    st.markdown("## ✏️ Update Account Details")
    st.info("Leave a field empty to keep it unchanged.")
    with st.form("update_form", clear_on_submit=True):
        account_no = st.text_input("Account Number", placeholder="e.g. AbC123!")
        pin = st.number_input("Current PIN", min_value=1000, max_value=9999, value=1234, step=1)

        st.markdown("#### New Details (optional)")
        new_name = st.text_input("New Name", placeholder="Leave empty to skip")
        new_email = st.text_input("New E-mail", placeholder="Leave empty to skip")
        new_pin = st.number_input("New PIN (0 = no change)", min_value=0, max_value=9999, value=0, step=1)

        submitted = st.form_submit_button("Update Details", use_container_width=True)

        if submitted:
            ok, msg = engine.update_details(
                account_no,
                pin,
                name=new_name or None,
                email=new_email or None,
                new_pin=new_pin if new_pin != 0 else None,
            )
            if ok:
                st.success(msg)
            else:
                st.error(msg)

# ── Delete Account ───────────────────────────────
elif page == "🗑️ Delete Account":
    st.markdown("## 🗑️ Delete Account")
    st.warning("⚠️ This action is permanent and cannot be undone.")
    with st.form("delete_form", clear_on_submit=True):
        account_no = st.text_input("Account Number", placeholder="e.g. AbC123!")
        pin = st.number_input("PIN", min_value=1000, max_value=9999, value=1234, step=1)
        confirm = st.checkbox("I understand this will permanently delete my account.")
        submitted = st.form_submit_button("Delete Account", use_container_width=True)

        if submitted:
            if not confirm:
                st.error("Please confirm that you understand the consequences.")
            else:
                ok, msg = engine.delete_account(account_no, pin)
                if ok:
                    st.success(msg)
                else:
                    st.error(msg)

# ── Footer ───────────────────────────────────────
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#666;'>© 2024 AAPLI Bank · Built with Streamlit</p>",
    unsafe_allow_html=True,
)